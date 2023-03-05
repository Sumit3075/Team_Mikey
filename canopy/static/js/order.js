var total = 0;
function update_total()
 {
   document.getElementById('Total').innerHTML = `₹${total}`;
 }
function increment(elementId) 
{
    let elemId = `val${elementId}`;
    console.log(elemId);
    let element = document.getElementById(elemId);
    element.value++;
    total += 349;
    let rateid = `rate${elementId}`;
    console.log(rateid);
    document.getElementById(rateid).innerHTML = `₹${element.value * 349}` ;
    update_total();
   //  let total = document.getElementById('Total');
   //  total.value += 349;
   //  document.getElementById('Total').innerHTML = `₹${total.value}`;
   

 }
 function decrement(elementId)
 {
    let elemId = `val${elementId}`;
    console.log(elemId);
    let element = document.getElementById(elemId);
    element.value--;
    total -= 349;
    let rateid = `rate${elementId}`;
    console.log(rateid);
    document.getElementById(rateid).innerHTML = `₹${element.value * 349}` ;
    update_total();
   //  let total = document.getElementById('Total');
   //  total.value -= 349;
   //  document.getElementById('Total').innerHTML = `₹${total.value}`;
 }
 