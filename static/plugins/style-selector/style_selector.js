$(document).ready(function () {
    "use strict";
    $(".style-settings select option[selected]").prop("selected", true);
    $(".style-settings select input[checked]").prop("checked", true);
    $(".style-settings-icon").click(function () {
        $(this).parent().toggleClass("opened");
    });
    $(".style-settings [name='color_scheme']").change(function () {
        if ($(this).val() === "skin-dark") {
            $("body").addClass("skin-dark");
        } else {
            $("body").removeClass("skin-dark");
        }
    });
});