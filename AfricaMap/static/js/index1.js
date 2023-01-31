let header =  document.getElementById('header')
let txt1 =  document.getElementById('logo-state')
let txt2 =  document.getElementById('logo-Location')
let input1 = document.getElementById('inp1')
let input2 = document.getElementById('inp2')
const search = document.getElementById('ser-1')
const search2 = document.getElementById('ser-2')
const section1 = document.getElementById('sec-1')
const section2 = document.getElementById('sec-2')


window.onscroll = function() {
  let kickOff =  window.pageYOffset
  if(kickOff <= 500) {
    header.style.background = "rgba(0, 0, 0, 0.509)" 
    txt1.style.color = 'rgba(0, 0, 0, 0.442)'
    txt2.style.color = 'rgba(0, 0, 0, 0.442)'
  }
  if(kickOff >= 500) {
    header.style.background = "black"
    txt1.style.color = 'white'
    txt2.style.color = 'white'      
  }
}




input1.oninput = function() {
   let inputText = this.value
   let node = document.getElementById('node')
  
   if(inputText.length < 1) {
     node.style.display = "none"
   } 
}

input2.oninput = function() {
  let inputText = this.value
  let node = document.getElementById('node1')
  console.log(node)
  if(inputText.length < 1) {
    node.style.display = "none"
  } 
}

function Temp(res) {
let results = `<div class="country-head">
                <h3><span class="cons">Country:</span> ${res.country}</h3>
              </div>
     <div class="con">
         <div class="A-1">
             <img src="${res.img}" alt="Abuja">
          </div>
     </div> 
     <div class="states">
         <div class="div-1">
             <img src="${res.img}" alt="Abuja">
         </div>
         <div class="div-2">
            <h4 id="city-1">${res.city1}</h4>
          <p class="A">
               <span>Polical History:</span> In the course of the examination, you are not permitted to 
               click outside of the examination page, on your computer, for another tab or any 
               other application for whatever reason, including for use of system calculator.
          </p>
         </div>  
    </div>
    <div class="states">
        <div class="div-1">
            <img src="${res.img}" alt="Abuja">
         </div>
         <div class="div-2">
            <h4 id="city-2">${res.city2}</h4>
          <p class="A">
               <span>Polical History:</span> In the course of the examination, you are not permitted to 
               click outside of the examination page, on your computer, for another tab or any 
               other application for whatever reason, including for use of system calculator.
          </p>
         </div>  
    </div>
    <div class="states">
        <div class="div-1">
            <img src="${res.img}" alt="Abuja">
         </div>
         <div class="div-2">
            <h4 id="city-3">${res.city3}</h4>
          <p class="A">
               <span>Polical History:</span> In the course of the examination, you are not permitted to 
               click outside of the examination page, on your computer, for another tab or any 
               other application for whatever reason, including for use of system calculator.
          </p>
         </div>  
    </div>
    <div class="states">
        <div class="div-1">
            <img src="${res.img}" alt="Abuja">
         </div>
         <div class="div-2">
            <h4 id="city-4">${res.city4}</h4>
          <p class="A">
               <span>Polical History:</span> In the course of the examination, you are not permitted to 
               click outside of the examination page, on your computer, for another tab or any 
               other application for whatever reason, including for use of system calculator.
          </p>
         </div>  
    </div>`
    return results
}

search.onclick = async ()=> {
     console.log(input1.value)
      if(input1.value === "") {
          return null
      }
      try {
        let response = await  fetch(`http://localhost:8000/${input1.value}`)
        let data = await response.json()
        console.log(data)
        let result =  Temp(data)
        let nodes = document.createElement('div')
        nodes.id = "node"
        nodes.innerHTML = result
        section1.appendChild(nodes)
        console.log(section1) 
      } catch(e) {
          console.log(e)
      }

}


search2.onclick = async ()=> {
  console.log(input2.value)
   if(input2.value === "") {
       return null
   }
   try {
     let response = await  fetch(`http://localhost:7000/${input2.value}`)
     let data = await response.json()
     console.log(data)
     let result =  Temp(data)
     let nodes = document.createElement('div')
     nodes.id = "node1"
     nodes.innerHTML = result
     section2.appendChild(nodes)
     console.log(section1) 
   } catch(e) {
       console.log(e)
   }

}