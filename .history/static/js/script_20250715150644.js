console.log("Valve configurator ready.");

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

  // OrbitControls
  const controls = new THREE.OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.05;
  controls.screenSpacePanning = false;
  controls.minDistance = 0.5;
  controls.maxDistance = 10;

  // Lighting
  const light = new THREE.HemisphereLight(0xffffff, 0x444444);
  scene.add(light);

  // Load the model
  const loader = new THREE.GLTFLoader();
  loader.load(
    "/static/models/KnifeGateValve.gltf",
    function (gltf) {
      const model = gltf.scene;
      model.scale.set(0.5, 0.5, 0.5);
      model.rotation.y = Math.PI;
      scene.add(model);
    },
    undefined,
    function (error) {
      console.error("Error loading 3D model:", error);
    }
  );

  camera.position.set(0, 0, 2);

  // Animate
  function animate() {
    requestAnimationFrame(animate);
    controls.update(); // ← required for damping
    renderer.render(scene, camera);
  }
  animate();
}
