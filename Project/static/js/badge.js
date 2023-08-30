var app = angular.module('app', ['ngAnimate'])

app.directive('animateChange', function($animate) {
  return function(scope, elem, attr) {
      var current;
      scope.$watch(attr.animateChange, function(nv, ov) {
        if (nv != ov) {
            var c = 'change';
            current && $animate.cancel(current);
            current = $animate.addClass(elem,c);
            current.then(function() {
              current = $animate.removeClass(elem,c);
            });
        }

      })
  }
})