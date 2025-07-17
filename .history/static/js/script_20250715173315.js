console.log("✅ Valve configurator ready.");

const viewer = document.getElementById("viewer");

if (viewer && typeof THREE !== 'undefined') {
  // Initialize the scene
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0xf0f0f0); // Light gray background

  // Set up camera
  const camera = new THREE.PerspectiveCamera(
    75,
    viewer.clientWidth / viewer.clientHeight,
    0.1,
    1000
  );
  camera.position.set(0, 1, 3);

  // Set up renderer
  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(viewer.clientWidth, viewer.clientHeight);
  viewer.appendChild(renderer.domElement);

  // Ambient and directional lighting
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
  scene.add(ambientLight);

  const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
  directionalLight.position.set(5, 10, 7.5);
  scene.add(directionalLight);

  // OrbitControls for mouse/touch rotation
  const controls = new THREE.OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.1;
  controls.minDistance = 1;
  controls.maxDistance = 10;

  // Load GLTF model
  const loader = new THREE.GLTFLoader();
  loader.load(
    "/static/models/ClarksonValve.gltf",  // Adjust path if needed
    (gltf) => {
      const model = gltf.scene;
      model.scale.set(1, 1, 1);
      model.rotation.y = Math.PI;
      model.position.set(0, -0.5, 0);  // Lower the model
      scene.add(model);
      console.log("✅ 3D model loaded.");
    },
    undefined,
    (error) => {
      console.error("❌ Error loading 3D model:", error);
    }
  );

  // Animation loop
  function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
  }

  animate();

  // Handle browser resize
  window.addEventListener("resize", () => {
    const width = viewer.clientWidth;
    const height = viewer.clientHeight;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
  });
} else {
  console.error("❌ THREE is not defined or viewer div not found.");
}
