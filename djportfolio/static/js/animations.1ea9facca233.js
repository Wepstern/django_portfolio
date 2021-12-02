window.addEventListener('load', event => { 
    
    // Navbar hide/show
    let prevScrollpos = window.pageYOffset;
    let navigator = document.getElementById("navigator");

    if(prevScrollpos != 0) {
        navigator.classList.remove("show-me");
        navigator.classList.add("hide-me");
    }

    window.onscroll = function() {
        let currentScrollPos = window.pageYOffset;

        if(prevScrollpos > currentScrollPos) {
            navigator.classList.remove("hide-me");
            navigator.classList.add("show-me");
        } 
        if(prevScrollpos < currentScrollPos && currentScrollPos > 100) {
            navigator.classList.remove("show-me");
            navigator.classList.add("hide-me");
        }
        if(currentScrollPos == 0) {
            navigator.classList.remove("hide-me");
            navigator.classList.remove("show-me");
        }
        prevScrollpos = currentScrollPos;
    }

    // Profile picture hover
    let userProfilePicture = document.getElementById("userProfilePicture");

    userProfilePicture.addEventListener("mouseover", function( event ) {
        userProfilePicture.classList.remove("gs-filter");
      }, false);

      userProfilePicture.addEventListener("mouseout", function( event ) {
        userProfilePicture.classList.add("gs-filter");
      }, false);

    // Experience hover
    let experience = document.querySelectorAll(".experience");

    experience.forEach(function(element) {
        element.addEventListener("mouseover", function( event ) {
            element.classList.add("bg-altfourth");
        }, false);
    });

    experience.forEach(function(element) {
        element.addEventListener("mouseout", function( event ) {
            element.classList.remove("bg-altfourth");
        }, false);
    });

    // Expertise cards
    class Card {
        constructor(
            // Card view small
            smExpertiseCards,
            smExpertiseCard,
            smExpertiseShowMoreButton,
            // Card view large
            lgExpertiseContainer,
            lgExpertiseCards,
            lgExpertiseCard,
            lgExpertiseShowLessButton)
        {
            
            (function () {
                lgExpertiseShowLessButton.addEventListener("click", function( event ) {
                    lgExpertiseContainer.classList.add("d-none");
                    lgExpertiseCard.classList.add("d-none");
                    smExpertiseCard.classList.remove("d-none");
                }, false);
                })();
            
            (function () {
                smExpertiseShowMoreButton.addEventListener("click", function( event ) {
                    lgExpertiseCards.forEach(function (element) {
                        if (!element.classList.contains("d-none")) {
                            element.classList.add("d-none");
                        }
                    })
                    smExpertiseCards.forEach(function (element) {
                        if (element.classList.contains("d-none")) {
                            element.classList.remove("d-none");
                        }
                    })
                    lgExpertiseContainer.classList.remove("d-none");
                    lgExpertiseCard.classList.remove("d-none");
                    smExpertiseCard.classList.add("d-none");

                }, false);
                })();
        }
    }

    //  Card view small
    let smExpertiseCards = document.querySelectorAll('[id^=smExpertiseCard]');
    let smExpertiseShowMoreButtons = document.querySelectorAll('[id^=smExpertiseShowMore]');

    // Card view large
    let lgExpertiseContainer = document.getElementById("lgExpertiseContainer");
    let lgExpertiseCards = document.querySelectorAll('[id^=lgExpertiseCard]');
    let lgExpertiseShowLessButtons = document.querySelectorAll('[id^=lgExpertiseShowLess]');

    for (let i = 0; i < smExpertiseCards.length; i++) {
        let card = new Card(
            //  Card view small 
            smExpertiseCards,
            smExpertiseCards[i],
            smExpertiseShowMoreButtons[i], 
            // Card view large
            lgExpertiseContainer,
            lgExpertiseCards,
            lgExpertiseCards[i],
            lgExpertiseShowLessButtons[i])
    }
});