app.factory('FilmsService', ['AppConfig', '$http', '$q', function(AppConfig, $http, $q) {
    var service = {};

    service.getFilms = function(options) {
        var defer = $q.defer();
        var url = AppConfig.generateURL('/films/');
        var uri = new URI(url);
        var filters = {};
        if (options) {
            angular.forEach(options, function(value, key) {
                if (value != '') filters[key] = value;
            });
        }
        uri.query(filters);
        $http.get(uri.toString()).success(function(data) {
            defer.resolve(data);
        });

        return defer.promise;
    };

    return service;
}]);