import React, { useState } from 'react';

interface Topic {
  name: string;
  hours: number;
  objectives: string[];
  standards: string[];
}

interface GradeData {
  title: string;
  total_hours: number;
  weekly_hours: number;
  topics: Topic[];
}

interface CurriculumModuleProps {
  grade: string;
  section: string;
  gradeData: GradeData;
  onTopicSelect: (topic: Topic) => void;
}

const CurriculumModule: React.FC<CurriculumModuleProps> = ({
  grade,
  section,
  gradeData,
  onTopicSelect
}) => {
  const [expandedTopic, setExpandedTopic] = useState<string | null>(null);

  const toggleTopic = (topicName: string) => {
    setExpandedTopic(expandedTopic === topicName ? null : topicName);
  };

  return (
    <div className="curriculum-module bg-white rounded-xl border shadow-sm p-6">
      {/* Module Header */}
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-2">
          {gradeData.title}
        </h2>
        <div className="flex items-center gap-4 text-sm text-gray-600">
          <span className="flex items-center">
            <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            Вкупно часови: {gradeData.total_hours}
          </span>
          <span className="flex items-center">
            <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v6a2 2 0 002 2h6a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
            Неделно: {gradeData.weekly_hours} часа
          </span>
        </div>
      </div>

      {/* Topics List */}
      <div className="space-y-4">
        <h3 className="text-lg font-semibold text-gray-700 mb-4">
          Наставни единици ({gradeData.topics.length})
        </h3>

        {gradeData.topics.map((topic, index) => (
          <div
            key={index}
            className="topic-card border border-gray-200 rounded-lg overflow-hidden hover:shadow-md transition-shadow"
          >
            {/* Topic Header */}
            <div
              className="topic-header bg-gray-50 px-4 py-3 cursor-pointer flex items-center justify-between"
              onClick={() => toggleTopic(topic.name)}
            >
              <div className="flex items-center">
                <h4 className="font-medium text-gray-800">{topic.name}</h4>
                <span className="ml-2 text-xs bg-blue-100 text-blue-800 px-2 py-1 rounded">
                  {topic.hours}ч
                </span>
              </div>
              <div className="flex items-center">
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    onTopicSelect(topic);
                  }}
                  className="mr-3 px-3 py-1 bg-indigo-100 text-indigo-700 rounded hover:bg-indigo-200 transition-colors text-sm"
                >
                  Избери
                </button>
                <svg
                  className={`w-5 h-5 text-gray-500 transform transition-transform ${
                    expandedTopic === topic.name ? 'rotate-180' : ''
                  }`}
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </div>
            </div>

            {/* Topic Details */}
            {expandedTopic === topic.name && (
              <div className="topic-details p-4 bg-white border-t border-gray-200">
                {/* Learning Objectives */}
                <div className="mb-4">
                  <h5 className="font-medium text-gray-700 mb-2 flex items-center">
                    <svg className="w-4 h-4 mr-2 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    Цели на учење
                  </h5>
                  <ul className="list-disc list-inside text-sm text-gray-600 space-y-1">
                    {topic.objectives.map((objective, objIndex) => (
                      <li key={objIndex}>{objective}</li>
                    ))}
                  </ul>
                </div>

                {/* Standards */}
                <div>
                  <h5 className="font-medium text-gray-700 mb-2 flex items-center">
                    <svg className="w-4 h-4 mr-2 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                    </svg>
                    Стандарди
                  </h5>
                  <ul className="list-disc list-inside text-sm text-gray-600 space-y-1">
                    {topic.standards.map((standard, stdIndex) => (
                      <li key={stdIndex}>{standard}</li>
                    ))}
                  </ul>
                </div>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default CurriculumModule;