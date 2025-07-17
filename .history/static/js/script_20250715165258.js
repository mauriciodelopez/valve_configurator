console.log("Valve configurator ready.");

// Obtener el div del visor
const viewer = document.getElementById("viewer");

if (viewer) {
  // Crear escena
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0xf2f2f2);

  // Cámara
  const camera = new THREE.PerspectiveCamera(
    75,
    viewer.clientWidth / viewer.clientHeight,
    0.1,
    1000
  );
  camera.position.set(0, 1, 3);

  // Renderizador
  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(viewer.clientWidth, viewer.clientHeight);
  viewer.appendChild(renderer.domElement);

  // Controles de órbita
  const controls = new THREE.OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.05;
  controls.minDistance = 1;
  controls.maxDistance = 10;

  // Luces
  const hemiLight = new THREE.HemisphereLight(0xffffff, 0x444444, 1);
  scene.add(hemiLight);

  const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
  dirLight.position.set(5, 10, 7.5);
  scene.add(dirLight);

  // Cargar modelo GLTF
  const loader = new THREE.GLTFLoader();
  loader.load(
    "/static/models/ClarksonValve.gltf",
    function (gltf) {
      const model = gltf.scene;
      model.scale.set(1, 1, 1);
      model.rotation.y = Math.PI;
      model.position.set(0, -0.5, 0);
      scene.add(model);
      console.log("✅ Modelo 3D cargado con éxito.");
    },
    undefined,
    function (error) {
      console.error("❌ Error cargando el modelo 3D:", error);
    }
  );

  // Animación
  function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
  }
  animate();

  // Ajustar tamaño al redimensionar ventana
  window.addEventListener("resize", () => {
    const width = viewer.clientWidth;
    const height = viewer.clientHeight;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
  });
}
