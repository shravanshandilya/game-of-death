var ctxMain = document.getElementById('my_canvas_main').getContext('2d');
var valueMain = parseInt(document.getElementById('my_canvas_main').getAttribute("value"));



//I know that this is a stupid piece of code,but it works :!



var ctx1 = document.getElementById('my_canvas1').getContext('2d');
var value1 = parseInt(document.getElementById('my_canvas1').getAttribute("value"));

var ctx2 = document.getElementById('my_canvas2').getContext('2d');
var value2 = parseInt(document.getElementById('my_canvas2').getAttribute("value"));

var ctx3 = document.getElementById('my_canvas3').getContext('2d');
var value3 = parseInt(document.getElementById('my_canvas3').getAttribute("value"));

var ctx4 = document.getElementById('my_canvas4').getContext('2d');
var value4 = parseInt(document.getElementById('my_canvas4').getAttribute("value"));

var al = 0;
var start = 4.72;
var cw = ctx1.canvas.width;
var ch = ctx1.canvas.height;
var diff;
var red = 0;
var green = 255;
var lineWidth = 20;
var radiusAdjustment = 10;
function rgb(r, g, b){
  return ["rgb(",r,",",g,",",b,")"].join("");
}





this.progressSimMain = function(){
	diff = ((al / 100) * Math.PI*2*10).toFixed(2);
	ctxMain.clearRect(0, 0, cw, ch);
	ctxMain.lineWidth = lineWidth;
	ctxMain.fillStyle = '#09F';
	ctxMain.strokeStyle = rgb(red,green,0);
	ctxMain.textAlign = 'center';
	ctxMain.font = '20pt Calibri';
	//ctx1.fillText(""+valueMain);
	ctxMain.fillText(valueMain+'%', cw*.5, ch*.5+2, cw);
	ctxMain.beginPath();
	ctxMain.arc(cw/2, ch/2, cw/2-radiusAdjustment, start, diff/10+start, false);
	ctxMain.stroke();
	if(al >= valueMain){
		clearTimeout(simMain);
	}
	al++;
	red = red +2;
	green = green -2;
}


















this.progressSim1 = function(){
	diff = ((al / 100) * Math.PI*2*10).toFixed(2);
	ctx1.clearRect(0, 0, cw, ch);
	ctx1.lineWidth = lineWidth;
	ctx1.fillStyle = '#09F';
	ctx1.strokeStyle = rgb(red,green,0);
	ctx1.textAlign = 'center';
	ctx1.font = '20pt Calibri';
	//ctx1.fillText(""+value1);
	ctx1.fillText(value1+'%', cw*.5, ch*.5+2, cw);
	ctx1.beginPath();
	ctx1.arc(cw/2, ch/2, cw/2-radiusAdjustment, start, diff/10+start, false);
	ctx1.stroke();
	if(al >= value1){
		clearTimeout(sim1);
	}
	al++;
	red = red +2;
	green = green -2;
}

this.progressSim2 = function(){
	diff = ((al / 100) * Math.PI*2*10).toFixed(2);
	ctx2.clearRect(0, 0, cw, ch);
	ctx2.lineWidth = lineWidth;
	ctx2.fillStyle = '#09F';
	ctx2.strokeStyle = rgb(red,green,0);
	ctx2.textAlign = 'center';
	ctx2.font = '20pt Calibri';
	//ctx2.fillText(""+value2);
	ctx2.fillText(value2+'%', cw*.5, ch*.5+2, cw);
	ctx2.beginPath();
	ctx2.arc(cw/2, ch/2, cw/2-radiusAdjustment, start, diff/10+start, false);
	ctx2.stroke();
	if(al >= value2){
		clearTimeout(sim2);
	}
	al++;
}

this.progressSim3 = function(){
	diff = ((al / 100) * Math.PI*2*10).toFixed(2);
	ctx3.clearRect(0, 0, cw, ch);
	ctx3.lineWidth = lineWidth;
	ctx3.fillStyle = '#09F';
	ctx3.strokeStyle = rgb(red,green,0);
	ctx3.textAlign = 'center';
	ctx3.font = '20pt Calibri';
	ctx3.fillText(value3+'%', cw*.5, ch*.5+2, cw);
	//ctx3.fillText(""+value3);
	ctx3.beginPath();
	ctx3.arc(cw/2, ch/2, cw/2-radiusAdjustment, start, diff/10+start, false);
	ctx3.stroke();
	if(al >= value3){
		clearTimeout(sim3);
	}
	al++;
}

this.progressSim4 = function(){
	diff = ((al / 100) * Math.PI*2*10).toFixed(2);
	ctx4.clearRect(0, 0, cw, ch);
	ctx4.lineWidth = lineWidth;
	ctx4.fillStyle = '#09F';
	ctx4.strokeStyle = rgb(red,green,0);
	ctx4.textAlign = 'center';
	ctx4.font = '20pt Calibri';
	ctx4.fillText(value4+'', cw*.5, ch*.5+2, cw);
	//ctx4.fillText(""+value4);
	ctx4.beginPath();
	ctx4.arc(cw/2, ch/2, cw/2-radiusAdjustment, start, diff/10+start, false);
	ctx4.stroke();
	if(al >= value4){
		clearTimeout(sim4);
	}
	al++;
}
this.color_updater = function(){
	if(red < 255){
		red = red + 5;
	}
	if(green > 0){
		green = green - 5;
	}
}
var sim1 = setInterval(progressSim1.bind(), 50);
var sim2 = setInterval(progressSim2.bind(), 50);
var sim3 = setInterval(progressSim3.bind(), 50);
var sim4 = setInterval(progressSim4.bind(), 50);
var simMain = setInterval(progressSimMain.bind(),50);
var colour = setInterval(color_updater.bind(),50);
