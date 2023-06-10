var selectElement = document.getElementById("id_estado");
var estado = selectElement.options[selectElement.selectedIndex].value;
// Acessar o valor do atributo 'data-filtro-cidade'
var filtroCidade = document.currentScript.getAttribute('data-filtro-cidade');
console.log(filtroCidade);
console.log(estado);

if (estado !== "todos") {
  console.log(estado);
  // Enviar uma solicitação AJAX para buscar as cidades correspondentes
  $.ajax({
    url: "/buscar_cidades/", // URL para a view Django que irá lidar com a solicitação
    type: 'get',
    data: {
      'estado': estado // Enviar o estado selecionado como parâmetro
    },
    success: function(data) {
      // Limpar as opções atuais do campo de cidade
      $('#id_cidade').empty();
      console.log(filtroCidade);

      // Adicionar as novas opções do campo de cidade com base na resposta recebida
      $.each(data.opcoes_cidades, function(index, cidade) {
        $('#id_cidade').append($('<option></option>').val(cidade[0]).text(cidade[1]));
      });
      
      // Selecionar no select o campo com o valor da variável 'filtroCidade'
      $('#id_cidade option[value="' + filtroCidade + '"]').prop('selected', true);
    }
  });
}


$(document).ready(function () {
  // Capturar o evento de mudança do campo de estado
  $('#id_estado').change(function () {
    var estado = $(this).val(); // Obter o valor do estado selecionado
    console.log(estado)

    // Enviar uma solicitação AJAX para buscar as cidades correspondentes
    $.ajax({
      url: "/buscar_cidades/",// URL para a view Django que irá lidar com a solicitação
      type: 'get',
      data: {
        'estado': estado // Enviar o estado selecionado como parâmetro
      },
      success: function (data) {
        // Limpar as opções atuais do campo de cidade
        $('#id_cidade').empty();

        // Adicionar as novas opções do campo de cidade com base na resposta recebida
        $.each(data.opcoes_cidades, function (index, cidade) {
          $('#id_cidade').append($('<option></option>').val(cidade[0]).text(cidade[1]));
        });
      }
    });
  });
});