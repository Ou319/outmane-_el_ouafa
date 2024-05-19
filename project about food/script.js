// document.addEventListener("DOMContentLoaded", () => {
//     const boxes = document.querySelectorAll('.box');
  
//     const observerOptions = {
//       root: null, // Use the viewport as the root
//       rootMargin: '0px',
//       threshold: 0.1 // 10% of the element should be active
//     };
  
//     const observerCallback = (entries, observer) => {
//       entries.forEach(entry => {
//         if (entry.isIntersecting) {
//           entry.target.classList.add('active');
//         } else {
//           entry.target.classList.remove('active');
//         }
//       });
//     };
  
//     const observer = new IntersectionObserver(observerCallback, observerOptions);
  
//     boxes.forEach(box => observer.observe(box));
//   });
  

// scrool nav bar here
let scrool1 =window.pageYOffset;
window.onscroll=function(){
    let scrool2=window.pageYOffset;
    if(scrool1 > scrool2){
        document.querySelector('header').style.top="0";
        document.querySelector('header').classList.add("active");
    }
    else{
        document.querySelector('header').style.top="-100px";
        document.querySelector('header').classList.remove("active");
    }
    scrool1=scrool2;
}   


// about slider img
let btn_next = document.querySelector(".prev");
let btn_prev = document.querySelector(".back");
let listItem = document.querySelector('main .list');
let thumbnailDon = document.querySelector('.thumbnail');

btn_next.onclick = function(){
  showSlider('next');
}

btn_prev.onclick = function(){
  showSlider('prev');
}

function showSlider(type) {
  let itemSlider = document.querySelectorAll('main .list .item');
  let itemhumBnail = document.querySelectorAll('main .thumbnail .item');

  if (type === 'next') {
    // Move first item to the end
    listItem.appendChild(itemSlider[0]);
    thumbnailDon.appendChild(itemhumBnail[0]);

    // Remove active class from all items
    itemSlider.forEach(item => item.classList.remove('active'));
    itemhumBnail.forEach(item => item.classList.remove('active'));

    // Add active class to the first item
    itemSlider[0].classList.add('active');
    itemhumBnail[0].classList.add('active');
  } else {
    // Move last item to the beginning
    listItem.prepend(itemSlider[itemSlider.length - 1]);
    thumbnailDon.prepend(itemhumBnail[itemhumBnail.length - 1]);

    // Remove active class from all items
    itemSlider.forEach(item => item.classList.remove('active'));
    itemhumBnail.forEach(item => item.classList.remove('active'));

    // Add active class to the first item
    itemSlider[0].classList.add('active');
    itemhumBnail[0].classList.add('active');
  }
}
document.addEventListener('keydown', function(event) {
  if (event.key === 'ArrowRight') {
      // Right arrow key
      showSlider('next');
  } else if (event.key === 'ArrowLeft') {
      // Left arrow key
      showSlider('prev');
  }
});

// animate element at scrool serise

document.addEventListener('DOMContentLoaded', function () {
  const observerOptions = {
      threshold: 0.1 // Trigger when 10% of the element is active
  };

  const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
          if (entry.isIntersecting) {
              entry.target.classList.add('active');
              entry.target.classList.remove('hidden');
          } else {
              entry.target.classList.remove('active');
              entry.target.classList.add('hidden');
          }
      });
  }, observerOptions);

  const hiddenElements = document.querySelectorAll('.sec-01 .items .item');
  hiddenElements.forEach(el => observer.observe(el));
});
document.addEventListener('DOMContentLoaded', function () {
  const observerOptions = {
      threshold: 0.1 // Trigger when 10% of the element is active
  };

  const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
          if (entry.isIntersecting) {
              entry.target.classList.add('active');
              entry.target.classList.remove('hidden');
          } else {
              entry.target.classList.remove('active');
              entry.target.classList.add('hidden');
          }
      });
  }, observerOptions);

  const hiddenElements = document.querySelectorAll('.about-img-02');
  hiddenElements.forEach(el => observer.observe(el));
});
document.addEventListener('DOMContentLoaded', function () {
  const observerOptions = {
      threshold: 0.1 // Trigger when 10% of the element is active
  };

  const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
          if (entry.isIntersecting) {
              entry.target.classList.add('active');
              entry.target.classList.remove('hidden');
          } else {
              entry.target.classList.remove('active');
              entry.target.classList.add('hidden');
          }
      });
  }, observerOptions);

  const hiddenElements = document.querySelectorAll('.content-02');
  hiddenElements.forEach(el => observer.observe(el));
});
document.addEventListener('DOMContentLoaded', function () {
  const observerOptions = {
      threshold: 0.1 // Trigger when 10% of the element is active
  };

  const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
          if (entry.isIntersecting) {
              entry.target.classList.add('active');
              entry.target.classList.remove('hidden');
          } else {
              entry.target.classList.remove('active');
              entry.target.classList.add('hidden');
          }
      });
  }, observerOptions);

  const hiddenElements = document.querySelectorAll('.my_items .item-left');
  hiddenElements.forEach(el => observer.observe(el));
});
document.addEventListener('DOMContentLoaded', function () {
  const observerOptions = {
      threshold: 0.1 // Trigger when 10% of the element is active
  };

  const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
          if (entry.isIntersecting) {
              entry.target.classList.add('active');
              entry.target.classList.remove('hidden');
          } else {
              entry.target.classList.remove('active');
              entry.target.classList.add('hidden');
          }
      });
  }, observerOptions);

  const hiddenElements = document.querySelectorAll('.sec-03');
  hiddenElements.forEach(el => observer.observe(el));
});
