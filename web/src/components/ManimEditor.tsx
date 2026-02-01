import { useState, useEffect } from 'react';
import { t } from '../utils/i18n';

interface Template {
  id: string;
  title: string;
  grade: string;
  category: string;
  score: number;
  description: string;
}

interface ManimEditorProps {
  initialProblemId?: string;
}

export default function ManimEditor({ initialProblemId }: ManimEditorProps) {
  const [templates, setTemplates] = useState<Template[]>([]);
  const [selectedTemplate, setSelectedTemplate] = useState<Template | null>(null);
  const [templateContent, setTemplateContent] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [message, setMessage] = useState('');
  const [videoUrl, setVideoUrl] = useState('');
  const [renderQuality, setRenderQuality] = useState('low');

  // Load available templates on mount
  useEffect(() => {
    loadTemplates();
  }, []);

  // Load specific template when selected
  useEffect(() => {
    if (selectedTemplate) {
      loadTemplate(selectedTemplate.id);
    }
  }, [selectedTemplate]);

  // Auto-select initial problem if provided
  useEffect(() => {
    if (initialProblemId && templates.length > 0) {
      const template = templates.find(t => t.id === initialProblemId);
      if (template) {
        setSelectedTemplate(template);
      }
    }
  }, [initialProblemId, templates]);

  const loadTemplates = async () => {
    try {
      const response = await fetch('/api/manim-editor?action=list-templates');
      const data = await response.json();
      setTemplates(data.templates);
    } catch (error) {
      console.error('Failed to load templates:', error);
      setMessage(t('manim_editor.load_templates_failed'));
    }
  };

  const loadTemplate = async (problemId: string) => {
    try {
      setIsLoading(true);
      const response = await fetch(`/api/manim-editor?action=get-template&id=${problemId}`);
      const data = await response.json();
      setTemplateContent(data.content);
      setMessage('');
    } catch (error) {
      console.error('Failed to load template:', error);
      setMessage('Failed to load template');
    } finally {
      setIsLoading(false);
    }
  };

  const saveTemplate = async () => {
    if (!selectedTemplate) return;

    try {
      setIsLoading(true);
      const response = await fetch('/api/manim-editor', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          action: 'save-template',
          problemId: selectedTemplate.id,
          content: templateContent
        })
      });

      const data = await response.json();
      if (data.success) {
        setMessage('Template saved successfully!');
      } else {
        setMessage('Failed to save template');
      }
    } catch (error) {
      console.error('Failed to save template:', error);
      setMessage('Failed to save template');
    } finally {
      setIsLoading(false);
    }
  };

  const renderTemplate = async () => {
    if (!selectedTemplate) return;

    try {
      setIsLoading(true);
      setMessage('Rendering video... This may take a few minutes.');
      setVideoUrl('');

      const response = await fetch('/api/manim-editor', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          action: 'render-template',
          problemId: selectedTemplate.id,
          quality: renderQuality
        })
      });

      const data = await response.json();
      if (data.success) {
        setVideoUrl(data.videoPath);
        setMessage('Video rendered successfully!');
      } else {
        setMessage(`Render failed: ${data.error}`);
      }
    } catch (error) {
      console.error('Failed to render template:', error);
      setMessage('Failed to render template');
    } finally {
      setIsLoading(false);
    }
  };

  const validateTemplate = async () => {
    if (!selectedTemplate) return;

    try {
      const response = await fetch('/api/manim-editor', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          action: 'validate-template',
          problemId: selectedTemplate.id
        })
      });

      const data = await response.json();
      if (data.valid) {
        setMessage('Template validation passed!');
      } else {
        setMessage(`Validation issues: ${data.issues.join(', ')}`);
      }
    } catch (error) {
      console.error('Failed to validate template:', error);
      setMessage('Failed to validate template');
    }
  };

  return (
    <div className="max-w-6xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6 text-center">
        {t('manim_editor.title')}
      </h1>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Template Selection */}
        <div className="lg:col-span-1">
          <h2 className="text-xl font-semibold mb-4">{t('manim_editor.select_template')}</h2>
          <div className="space-y-2 max-h-96 overflow-y-auto">
            {templates.map((template) => (
              <div
                key={template.id}
                className={`p-3 border rounded cursor-pointer hover:bg-gray-50 ${
                  selectedTemplate?.id === template.id ? 'border-blue-500 bg-blue-50' : 'border-gray-200'
                }`}
                onClick={() => setSelectedTemplate(template)}
              >
                <div className="font-medium">{template.title}</div>
                <div className="text-sm text-gray-600">
                  Grade {template.grade} • {template.category} • Score: {template.score}
                </div>
                <div className="text-sm text-gray-500 mt-1">
                  {template.description.length > 60
                    ? template.description.substring(0, 60) + '...'
                    : template.description}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Editor */}
        <div className="lg:col-span-2">
          {selectedTemplate && (
            <>
              <div className="mb-4 flex justify-between items-center">
                <h2 className="text-xl font-semibold">
                  {t('manim_editor.editing').replace('{{title}}', selectedTemplate.title)}
                </h2>
                <div className="flex gap-2">
                  <select
                    value={renderQuality}
                    onChange={(e) => setRenderQuality(e.target.value)}
                    className="border rounded px-2 py-1 text-sm"
                  >
                    <option value="low">{t('manim_editor.low_quality')}</option>
                    <option value="medium">{t('manim_editor.medium_quality')}</option>
                    <option value="high">{t('manim_editor.high_quality')}</option>
                    <option value="ultra">{t('manim_editor.ultra_quality')}</option>
                  </select>
                </div>
              </div>

              {/* Action Buttons */}
              <div className="mb-4 flex gap-2 flex-wrap">
                <button
                  onClick={saveTemplate}
                  disabled={isLoading}
                  className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 disabled:opacity-50"
                >
                  {isLoading ? t('manim_editor.saving') : t('manim_editor.save_template')}
                </button>
                <button
                  onClick={validateTemplate}
                  disabled={isLoading}
                  className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 disabled:opacity-50"
                >
                  {t('manim_editor.validate')}
                </button>
                <button
                  onClick={renderTemplate}
                  disabled={isLoading}
                  className="bg-purple-500 text-white px-4 py-2 rounded hover:bg-purple-600 disabled:opacity-50"
                >
                  {isLoading ? t('manim_editor.rendering') : t('manim_editor.render_video')}
                </button>
              </div>

              {/* Message Display */}
              {message && (
                <div className={`mb-4 p-3 rounded ${
                  message.includes('success') || message.includes('passed')
                    ? 'bg-green-100 text-green-800'
                    : 'bg-red-100 text-red-800'
                }`}>
                  {message}
                </div>
              )}

              {/* Code Editor */}
              <div className="mb-4">
                <textarea
                  value={templateContent}
                  onChange={(e) => setTemplateContent(e.target.value)}
                  className="w-full h-96 font-mono text-sm border rounded p-3"
                  placeholder="Template content will appear here..."
                  spellCheck={false}
                />
              </div>

              {/* Video Preview */}
              {videoUrl && (
                <div className="mt-6">
                  <h3 className="text-lg font-semibold mb-2">Rendered Video Preview</h3>
                  <video
                    controls
                    className="w-full max-w-2xl border rounded"
                    src={videoUrl}
                  >
                    Your browser does not support the video tag.
                  </video>
                </div>
              )}
            </>
          )}

          {!selectedTemplate && (
            <div className="text-center text-gray-500 mt-12">
              <div className="text-6xl mb-4">🎬</div>
              <div className="text-xl">Select a template to start editing</div>
              <div className="text-sm mt-2">
                Choose from {templates.length} available Manim templates
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Instructions */}
      <div className="mt-8 bg-blue-50 p-4 rounded">
        <h3 className="font-semibold mb-2">How to Use:</h3>
        <ol className="list-decimal list-inside space-y-1 text-sm">
          <li>Select a template from the list on the left</li>
          <li>Edit the Python code in the text area</li>
          <li>Click "Validate" to check for issues</li>
          <li>Click "Save Template" to save your changes</li>
          <li>Click "Render Video" to generate the animation</li>
          <li>Watch the video preview below when complete</li>
        </ol>
      </div>
    </div>
  );
}