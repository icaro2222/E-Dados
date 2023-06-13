
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

  var selectElement = document.getElementById("id_amostra");
  var selectedOption = selectElement.options[selectElement.selectedIndex].value;
  
  if (selectedOption == "todos_os_dados") {
    document.getElementById("preloader2").addEventListener("click", function() {
      document.getElementById("preloader").style.display = "block";
    });
  }else {
    document.getElementById("preloader2").addEventListener("click", function() {
      document.getElementById("preloader_processando").style.display = "block";
    });
  }
  
  
  selectElement.addEventListener("change", function() {
    selectedOption = selectElement.options[selectElement.selectedIndex].value;
  
    if (selectedOption == "todos_os_dados") {
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
  // var selectElement = document.getElementById("id_amostra");

  // selectElement.onchange = function() {
  //   var selectedOption = selectElement.options[selectElement.selectedIndex].value;
  
  //   if (selectedOption == "todos_os_dados") {
  //     document.getElementById("preloader2").addEventListener("click", function() {
  //       document.getElementById("preloader").style.display = "block";
  //     });
  //   }
  // }
  