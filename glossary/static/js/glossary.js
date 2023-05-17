$(function () {
  // Filter db_snapshot terms
  $('#db_snapshotFilter').on('keyup', function () {
    $('.definition').hide()
    $(`.definition:contains(${$(this).val()})`).show()
  })
});