app.factory('AppConfig', function(){
    var service = {
        baseURL: "http://localhost:8000"
    };
    
    service.generateURL = function(url) {
        return service.baseURL + url;
    };
    
    return service;
});