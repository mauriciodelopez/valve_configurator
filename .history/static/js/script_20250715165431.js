console.log("Valve configurator ready.");

const viewer = document.getElementById("viewer");

if (viewer) {
  // Initialize the 3D scene
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0xf2f2f2); // Light gray background

  // Set up the camera
  const camera = new THREE.PerspectiveCamera(
    75, // Field of view
    viewer.clientWidth / viewer.clientHeight, // Aspect ratio
    0.1, // Near clipping plane
    1000 // Far clipping plane
  );
  camera.position.set(0, 1, 3); // Move camera back to see the model

  // Create the renderer
  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(viewer.clientWidth, viewer.clientHeight);
  viewer.appendChild(renderer.domElement); // Add renderer to the viewer div

  // OrbitControls for mouse interaction
  const controls = new THREE.OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.05;
  controls.minDistance = 1;
  controls.maxDistance = 10;

  // Add ambient lighting
  const hemiLight = new THREE.HemisphereLight(0xffffff, 0x444444, 1);
  scene.add(hemiLight);

  // Add directional light for shadows and highlights
  const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
  dirLight.position.set(5, 10, 7.5);
  scene.add(dirLight);

  // Load the GLTF model
  const loader = new THREE.GLTFLoader();
  loader.load(
    "/static/models/ClarksonValve.gltf", // Path to your model
    function (gltf) {
      const model = gltf.scene;
      model.scale.set(1, 1, 1); // Resize model if needed
      model.rotation.y = Math.PI; // Optional: rotate model 180°
      model.position.set(0, -0.5, 0); // Lower the model for better centering
      scene.add(model);
      console.log("✅ 3D model loaded successfully.");
    },
    undefined,
    function (error) {
      console.error("❌ Failed to load 3D model:", error);
    }
  );

  // Animation loop
  function animate() {
    requestAnimationFrame(animate);
    controls.update(); // Update controls for damping
    renderer.render(scene, camera); // Render the scene
  }
  animate();

  // Adjust canvas on window resize
  window.addEventListener("resize", () => {
    const width = viewer.clientWidth;
    const height = viewer.clientHeight;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
  });
}
