console.log("Valve configurator ready.");

// Load 3D model with Three.js
const viewer = document.getElementById("viewer");

if (viewer) {
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(
    75,
    viewer.clientWidth / viewer.clientHeight,
    0.1,
    1000
  );
  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(viewer.clientWidth, viewer.clientHeight);
  viewer.appendChild(renderer.domElement);

  // Lighting
  const light = new THREE.HemisphereLight(0xffffff, 0x444444);
  scene.add(light);

  // Load the GLTF model
  const loader = new THREE.GLTFLoader();
  loader.load(
    "/static/models/KnifeGateValve.gltf",
    function (gltf) {
      const model = gltf.scene;
      model.scale.set(0.5, 0.5, 0.5); // Adjust scale if too big/small
      model.rotation.y = Math.PI;     // Rotate if needed
      scene.add(model);
    },
    undefined,
    function (error) {
      console.error("Error loading model:", error);
    }
  );

  camera.position.z = 2;

  // Animate
  function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
  }
  animate();
}
