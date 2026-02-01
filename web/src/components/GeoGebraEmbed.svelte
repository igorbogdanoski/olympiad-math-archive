<script>
  import { onMount } from 'svelte';

  export let materialId = ""; // GeoGebra Material ID
  export let ggbBase64 = "";   // Base64 encoded string of the .ggb file
  export let width = 800;
  export let height = 500;
  export let showMenuBar = false;
  export let showAlgebraInput = false;
  export let showToolBar = false;
  export let language = "mk";

  let container;

  onMount(() => {
    const params = {
      "appName": "geometry",
      "width": width,
      "height": height,
      "showToolBar": showToolBar,
      "showAlgebraInput": showAlgebraInput,
      "showMenuBar": showMenuBar,
      "enableLabelDrags": true,
      "enableShiftDragZoom": true,
      "enableRightClick": false,
      "showZoomButtons": true,
      "errorDialogsActive": true,
      "useBrowserForJS": false,
      "language": language
    };

    if (materialId) {
      params.materialId = materialId;
    } else if (ggbBase64) {
      params.ggbBase64 = ggbBase64;
    }
    
    if (window.GGBApplet) {
      const applet = new window.GGBApplet(params, true);
      applet.inject(container);
    }
  });
</script>

<svelte:head>
  <script src="https://www.geogebra.org/apps/deployggb.js"></script>
</svelte:head>

<div class="geogebra-container shadow-lg rounded-xl overflow-hidden border border-gray-200 bg-white p-2">
  <div bind:this={container}></div>
  <p class="text-xs text-gray-400 mt-2 text-center">Интерактивен GeoGebra аплет • TeacherOS Dynamic Learning</p>
</div>

<style>
  .geogebra-container {
    max-width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
</style>
