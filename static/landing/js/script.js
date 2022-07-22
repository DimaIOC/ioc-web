"use strict";

// header
(function () {
  $(".burger__icon").on("click", function () {
    $(this).toggleClass("active");
    $(".header-mobile").toggleClass("show");
  });
})();
// header end
// sliders
(function () {
  const servicesSlider = new Swiper(".services-slider", {
    spaceBetween: 0,
    loop: true,
    slidesPerView: 1,
    centeredSlides: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".service-button-next",
      prevEl: ".service-button-prev",
    },
    breakpoints: {
      1200: {
        slidesPerView: 3,
        spaceBetween: 80,
      },
      990: {
        slidesPerView: 3,
        spaceBetween: 80,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 50,
      },
    },
  });
  const partnersSlider = new Swiper(".partners-slider", {
    loop: true,
    slidesPerView: "auto",
    spaceBetween: 10,
    centeredSlides: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    breakpoints: {
      768: {
        slidesPerView: 5,
        spaceBetween: 20,
      },
      568: {
        slidesPerView: 3,
        spaceBetween: 20,
      },
    },
  });
  $(".partners-button-next").on("click", (e) => {
    partnersSlider.slideNext();
  });
  $(".partners-button-prev").on("click", (e) => {
    partnersSlider.slidePrev();
  });

  const teamSlider = new Swiper(".team__slider", {
    spaceBetween: 0,
    loop: true,
    slidesPerView: "auto",
    spaceBetween: 20,
    // centeredSlides: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    breakpoints: {
      768: {
        slidesPerView: 6,
      },
      568: {
        slidesPerView: 3,
      },
      440: {
        slidesPerView: 2,
      },
    },
  });
  $(".team-button-next").on("click", (e) => {
    teamSlider.slideNext();
  });
  $(".team-button-prev").on("click", (e) => {
    teamSlider.slidePrev();
  });
})();
// sliders end
// questions
(function () {
  $(".questions-item__head").on("click", function () {
    $(this).parent().toggleClass("show");
    $(this).parent().find($(".questions-item__body")).slideToggle();
  });
})();
// questions end

//requisites
(function () {
  $(".requsites-data__head").on("click", function () {
    $(this).parent().toggleClass("open");
  });
})();
//requisites end

// popups
(function () {
  function showPopup(el) {
    $(".popups").show();
    $(el).addClass("show");
  }
  function closePopup() {
    $(".popups").hide();
    $(".popup").removeClass("show");
  }
  $("[data-popup]").on("click", function (e) {
    e.preventDefault();

    let el = $(this).attr("data-popup");

    showPopup(el);
    timer(3, $(".timer"), null);
    // timer(3, $('.timer'), closePopup)
  });
  $(".js-close").on("click", function (e) {
    e.preventDefault();
    closePopup();
  });
  document.addEventListener("click", (e) => {
    if (e.target.className === "popups__inner") {
      closePopup();
    }
  });
})();
// popups end

// scroll-href
var $page = $("html, body");
$("[scroll-href]").click(function (e) {
  e.preventDefault();
  $page.animate(
    {
      scrollTop: $($.attr(this, "scroll-href")).offset().top,
    },
    400
  );
  return false;
});

// copy function
(function () {
  async function clipboardCopy(text) {
    await navigator.clipboard.writeText(text);
  }

  const copyBtns = document.querySelectorAll(".requsites-data__copy");
  copyBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      const copyedText = e.target
        .closest(".requsites-data__copy")
        .parentNode.querySelector(".requsites-data__text").textContent;
      clipboardCopy(copyedText);
    });
  });
})();


// gallery

$('.popup-gallery').magnificPopup({
  delegate: '.image-popup',
  type: 'image',
  tLoading: 'Loading image #%curr%...',
  mainClass: 'mfp-img-mobile',
  gallery: {
    enabled: true,
    navigateByImgClick: true,
    preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
  },
  image: {
    tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
    titleSrc: function (item) {
      return `
      <div class="team-catalog__item-info">
    ${item.el.attr('status') ?
          `<div>
      <i class="fa-solid fa-user"></i>
    ${item.el.attr('status')}
      </div>` : ''}
    ${item.el.attr('location') ? `<div>
        <i class="fa-solid fa-location-dot"></i>
    ${item.el.attr('location')}
      </div>` : ''}    
    ${item.el.attr('social') ? `<div>
    <i class="fa-solid fa-share-nodes"></i>
    ${item.el.attr('social')}
    </div>` : ''}    
    ${item.el.attr('phone') ? `<div>
    <i class="fa-solid fa-phone"></i>
    ${item.el.attr('phone')}
  </div>` : ''}    ${item.el.attr('email') ? `<a href="mailto:${item.el.attr('email')}">
  <i class="fa-solid fa-envelope"></i>
  ${item.el.attr('email')}
</a>` : ''}
       
      </div>
      `;
    }
  }
});

// gallery end