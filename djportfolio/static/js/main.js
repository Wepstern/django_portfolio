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
            // Card closed view small
            smClosedExpertiseCards,
            smClosedExpertiseCard,
            smClosedExpertiseShowMoreButton,
            // Card opened view small
            smOpenedExpertiseCards,
            smOpenedExpertiseCard,
            smOpenedExpertiseShowLessButton,
            // Card opened view large
            lgOpenedExpertiseContainer,
            lgOpenedExpertiseCards,
            lgOpenedExpertiseCard,
            lgOpenedExpertiseShowLessButton)
        {

            //hide opened small cards
            (function () {
                smOpenedExpertiseShowLessButton.addEventListener("click", function( event ) {
                    smOpenedExpertiseCard.classList.add("d-none");
                    smClosedExpertiseCard.classList.remove("d-none");
                }, false);
            })();

            //hide opened large cards
            (function () {
                lgOpenedExpertiseShowLessButton.addEventListener("click", function( event ) {
                    lgOpenedExpertiseContainer.classList.add("d-none");
                    lgOpenedExpertiseCard.classList.add("d-none");
                    smClosedExpertiseCard.classList.remove("d-none");
                }, false);
            })();

            //show opened large adn small hidden cards
            (function () {    
                smClosedExpertiseShowMoreButton.addEventListener("click", function( event ) {
                    lgOpenedExpertiseCards.forEach(function (element) {
                        if (!element.classList.contains("d-none")) {
                            element.classList.add("d-none");
                        }
                    })
                    smOpenedExpertiseCards.forEach(function (element) {
                        if (!element.classList.contains("d-none")) {
                            element.classList.add("d-none");
                        }
                    })
                    smClosedExpertiseCards.forEach(function (element) {
                        if (element.classList.contains("d-none")) {
                            element.classList.remove("d-none");
                        }
                    })
                    lgOpenedExpertiseContainer.classList.remove("d-none");
                    lgOpenedExpertiseCard.classList.remove("d-none");

                    smOpenedExpertiseCard.classList.remove("d-none");

                    smClosedExpertiseCard.classList.add("d-none");
                }, false);
                })();
        }
    }

    //  Card closed view small
    let smClosedExpertiseCards = document.querySelectorAll('[id^=smClosedExpertiseCard]');
    let smClosedExpertiseShowMoreButtons = document.querySelectorAll('[id^=smClosedExpertiseShowMore]');

    // Card opened view small
    let smOpenedExpertiseCards = document.querySelectorAll('[id^=smOpenedExpertiseCard]');
    let smOpenedExpertiseShowLessButtons = document.querySelectorAll('[id^=smOpenedExpertiseShowLess]');

    // Card opened view large
    let lgOpenedExpertiseContainer = document.getElementById("lgOpenedExpertiseContainer");
    let lgOpenedExpertiseCards = document.querySelectorAll('[id^=lgOpenedExpertiseCard]');
    let lgOpenedExpertiseShowLessButtons = document.querySelectorAll('[id^=lgOpenedExpertiseShowLess]');

    for (let i = 0; i < smClosedExpertiseCards.length; i++) {
        let card = new Card(
            //  Card closed view small 
            smClosedExpertiseCards,
            smClosedExpertiseCards[i],
            smClosedExpertiseShowMoreButtons[i], 
            // Card opened view small
            smOpenedExpertiseCards,
            smOpenedExpertiseCards[i],
            smOpenedExpertiseShowLessButtons[i],
            // Card opened view large
            lgOpenedExpertiseContainer,
            lgOpenedExpertiseCards,
            lgOpenedExpertiseCards[i],
            lgOpenedExpertiseShowLessButtons[i]
        )
    }
});