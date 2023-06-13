
  // Toggle the side navigation
  function imprimirComDelay() {
    setTimeout(function () {
      window.print();
    }, 100);
  }

  window.onload = function geraranalise() {
    var progressbar = document.getElementById("progressbar");
    var width = 0;
    var id = setInterval(frame, 10);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
      } else {
        width++;
        progressbar.style.width = width + '%';
      }
    }
  };
  
  

  document.getElementById("progressbar").style.animation = "none";

  window.addEventListener("load", function () {
    // Função chamada quando a página termina de carregar
    var loading_grafico = document.getElementById("loading_grafico");
      loading_grafico.style.display = "none";
  });

  var selectElement_id_amostra = document.getElementById("id_amostra");
  var selectedOption_id_amostra = selectElement_id_amostra.options[selectElement_id_amostra.selectedIndex].value;
  
  if (selectedOption_id_amostra == "todos_os_dados") {
    document.getElementById("preloader2").addEventListener("click", function() {
      document.getElementById("preloader").style.display = "block";
    });
  }else {
    document.getElementById("preloader2").addEventListener("click", function() {
      document.getElementById("preloader_processando").style.display = "block";
    });
  }
  
  
  selectElement_id_amostra.addEventListener("change", function() {
    selectedOption_id_amostra = selectElement_id_amostra.options[selectElement_id_amostra.selectedIndex].value;
  
    if (selectedOption_id_amostra == "todos_os_dados") {
      document.getElementById("preloader2").addEventListener("click", function() {
        document.getElementById("preloader_processando").style.display = "none";
        document.getElementById("preloader").style.display = "block";
      });
    }else{
      document.getElementById("preloader2").addEventListener("click", function() {
        document.getElementById("preloader").style.display = "none";
        document.getElementById("preloader_processando").style.display = "block";
      });
    }    
  });