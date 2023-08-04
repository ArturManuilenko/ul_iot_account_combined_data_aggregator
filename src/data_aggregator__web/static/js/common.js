function get_select_data_gateway(object){
    let $data = $(object)
    fetch('/data-gateway-select').then(function (response) {
          response.json().then(function (data) {
            let optionHTML = '';
            if (data.payload.length > 0) {
              optionHTML += '<option disabled selected></option>';
              for (let item of data.payload) {
                  optionHTML += '<option value="' + item.id + '">' + item.name + '</option>';
              }
              $data.html(optionHTML);
            }
            else {
              $data.html('<option disabled selected>None</option>');
            }
          });
        });

}


function get_select_data_gateway_network_id(object, id) {
    let $data = $(object)
    fetch('/data-gateway-network-select/' + id).then(function (response) {
        response.json().then( function (data) {
          let optionHTML = '';
          if (data.payload.length > 0) {
              optionHTML += '<option disabled selected>DATA-GATEWAY-NETWORK</option>';
              for (let data_gateway_network of data.payload) {
                optionHTML += '<option value="' + data_gateway_network.id + '">' + data_gateway_network.name + '</option>';
              }
              $data.html(optionHTML);
            }
            else {
              $data.html('<option disabled selected>None</option>');
            }
        });
      });
}


function get_select_protocol(object){
    let $data = $(object)
    fetch('/protocol-select').then(function (response) {
          response.json().then(function (data) {
            let optionHTML = '';
            if (data.payload.length > 0) {
              optionHTML += '<option disabled selected></option>';
              for (let item of data.payload) {
                  optionHTML += '<option value="' + item.id + '">' + item.name + '</option>';
              }
              $data.html(optionHTML);
            }
            else {
              $data.html('<option disabled selected>None</option>');
            }
          });
        });

}


function get_select_metering_type(object){
    let $data = $(object)
    fetch('/device-metering-type-select').then(function (response) {
          response.json().then(function (data) {
            let optionHTML = '';
            if (data.payload.length > 0) {
              optionHTML += '<option disabled selected></option>';
              for (let item of data.payload) {
                  optionHTML += '<option value="' + item.id + '">' + item.name_ru + '</option>';
              }
              $data.html(optionHTML);
            }
            else {
              $data.html('<option disabled selected>None</option>');
            }
          });
        });
}

function get_select_modification_type_by_id(object, id) {
    let $data = $(object)
    fetch('/device-modification-types-select/' + id).then(function (response) {
        response.json().then( function (data) {
          let optionHTML = '';
          if (data.payload.length > 0) {
              optionHTML += '<option disabled selected></option>';
              for (let modifications_type of data.payload) {
                optionHTML += '<option value="' + modifications_type.id + '">' + modifications_type.name_ru + '</option>';
              }
              $data.html(optionHTML);
            }
            else {
              $data.html('<option disabled selected>None</option>');
            }
        });
      });
}

function get_select_modification_by_id(object, id) {
    let $data = $(object)
    fetch('/device-modifications-select/' + id).then(function (response) {
        response.json().then( function (data) {
          let optionHTML = '';
          if (data.payload.length > 0) {
              optionHTML += '<option disabled selected></option>';
              for (let modifications of data.payload) {
                optionHTML += '<option value="' + modifications.id + '">' + modifications.name + '</option>';
              }
              $data.html(optionHTML);
            }
            else {
              $data.html('<option disabled selected>None</option>');
            }
        });
      });
}

function get_select_modifications(object){
    let $data = $(object)
    fetch('/device-modifications-select').then(function (response) {
          response.json().then(function (data) {
            let optionHTML = '';
            if (data.payload.length > 0) {
              optionHTML += '<option disabled selected></option>';
              for (let item of data.payload) {
                  optionHTML += '<option value="' + item.id + '">' + item.name + '</option>';
              }
              $data.html(optionHTML);
            }
            else {
              $data.html('<option disabled selected>None</option>');
            }
          });
        });

}

function get_select_manufacturer(object){
    let $data = $(object)
    fetch('/manufacturer-select').then(function (response) {
          response.json().then(function (data) {
            let optionHTML = '';
            if (data.payload.length > 0) {
              optionHTML += '<option disabled selected></option>';
              for (let item of data.payload) {
                  optionHTML += '<option value="' + item.id + '">' + item.name + '</option>';
              }
              $data.html(optionHTML);
            }
            else {
              $data.html('<option disabled selected>None</option>');
            }
          });
        });

}
