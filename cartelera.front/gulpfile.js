var gulp = require('gulp'),
  compass = require('gulp-compass'),
  notify = require("gulp-notify"),
  concat = require('gulp-concat'),
  uglify = require('gulp-uglify'),
  plumber = require('gulp-plumber'),
  clean = require('gulp-clean')
  ;

var title = 'Cartelera';

gulp.task('compass', ['clean-styles'], function() {
  gulp.src('sass/**/*.scss')
    .pipe(plumber({errorHandler: notify.onError({message: 'Commpass compile error', title: title})}))
    .pipe(compass({
      config_file: './config.rb'
    }))
    .pipe(notify('Finished compass!!'));
});

gulp.task('css_lib', function(){
  return gulp.src([

    ])
    .pipe(plumber({errorHandler: notify.onError({message: 'CSS concat error', title: title})}))
    .pipe(concat('lib.css'))
    .pipe(gulp.dest('css'));
});

gulp.task('minify', function(){
  return gulp.src([
    'js/**/*.js'
  ])
    .pipe(plumber({errorHandler: notify.onError({message: 'JS minify error', title: title})}))
    .pipe(concat('script.min.js'))
    .pipe(uglify({mangle:false}))
    .pipe(gulp.dest('dist'))
    .pipe(notify('Finished minification!!'));
});

gulp.task('minify_lib', function() {
  return gulp.src([
   
  ])
    .pipe(plumber({errorHandler: notify.onError({message: 'JS minify error', title: title})}))
    .pipe(concat('lib.min.js'))
    .pipe(uglify({mangle:false}))
    .pipe(gulp.dest('dist'));
});

gulp.task('clean-styles', function() {
  return gulp.src('css/style.css')
         .pipe(clean());
});

gulp.task('clean-scripts', function() {
  return gulp.src([
          'dist/script.min.js',
          'dist/lib.min.js'
         ])
          .pipe(clean());
});

gulp.task('clean-and-build-scripts', ['clean-scripts', 'minify', 'minify_lib'], function(){});

gulp.task('build', ['compass','css_lib', 'minify', 'minify_lib'], function() {});

gulp.task('default', ['compass','css_lib', 'minify', 'minify_lib'], function() {});

gulp.task('watch', function(){
  gulp.watch('sass/**/*.scss', ['compass']);
  gulp.watch('js/**/*.js', ['minify']);
});