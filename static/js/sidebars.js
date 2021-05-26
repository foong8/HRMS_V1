function openNav() {
    console.log('Helo')
  document.getElementById("_sidebar").style.width = "250px";
  document.getElementById("_content").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("_sidebar").style.width = "0";
  document.getElementById("_content").style.marginLeft= "0";
}