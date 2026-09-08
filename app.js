document.querySelectorAll('.nav').forEach(btn=>{
 btn.addEventListener('click',()=>{
   document.querySelectorAll('.nav').forEach(b=>b.classList.remove('active'));
   document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
   btn.classList.add('active');
   document.getElementById(btn.dataset.target).classList.add('active');
 });
});