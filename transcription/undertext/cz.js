$(document).ready(function() {
    $('.tooltip').tooltipster({
      contentAsHTML: true,
      debug: true,
      interactive: true
    });
    $('.tooltip-struc').tooltipster({
      contentAsHTML: true,
      debug: true,
      interactive: true,
      side: "left"
    });
    $('.tooltip-corr').tooltipster({
      contentAsHTML: true,
      debug: true,
      interactive: true,
      side: "bottom"
    });
});
