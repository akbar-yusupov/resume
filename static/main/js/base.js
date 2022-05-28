$( document ).ready(function() {
  if (request_path=='/ru/' || request_path=='/en/') {
    $('#home').addClass('text-decoration-underline');
  } else if (request_path.includes('portfolio')) {
    $('#portfolio').addClass('text-decoration-underline');
  } else if (request_path.includes('contact')) {
    $('#contact').addClass('text-decoration-underline');
  }
});