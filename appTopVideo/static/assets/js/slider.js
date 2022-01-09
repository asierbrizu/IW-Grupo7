
var slideIndex = 1;

showDivs(slideIndex);

function carga(){
	showDivs(1)
	automatico();
}

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function currentDiv(n) {
  showDivs(slideIndex = n);
}

function showDivs(n) {
	var i;
	var x = document.getElementsByClassName("imgSlider");
	if (n > x.length) {
		slideIndex = 1
	}
	if (n < 1) {
		slideIndex = x.length
	}
	for (i = 0; i < x.length; i++) {

		x[i].style.display = "none";  
	}
	x[slideIndex-1].style.display = "block";  
}

function automatico(){
	plusDivs(1);
	setTimeout(automatico, 4000);
}

