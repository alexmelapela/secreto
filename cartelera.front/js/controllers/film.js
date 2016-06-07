var app = angular.module("cartelera");

app.controller('FilmsController', ['$scope', '$element', 'FilmsService', function($scope, $element, FilmsService) {
    $scope.movies = [];
    FilmsService.getFilms().then(function(data) {
        $scope.movies = data;
    })


}]);