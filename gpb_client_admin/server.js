const serve = require('serve');

const server = serve('build', {
  port: 3000,
  ignore: ['node_modules']
});

console.log('Serving on http://localhost:3000');
