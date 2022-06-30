$(document).on('submit', 'form', function (e) {
  e.preventDefault();
  console.log($("form").serialize());

  $.ajax({
      type: 'POST',
      url: window.location.pathname,
      data: $('form').serialize(), // serializes the form's elements.
      success: function (data) {
        alert('Form submitted successfully');
      },
  });
});