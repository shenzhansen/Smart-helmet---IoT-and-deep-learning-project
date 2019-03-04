var Ip = new URL("http://51.91.78.255:80");
trip_params = {query:'trip'};
Object.keys(trip_params).forEach(key => Ip.searchParams.append(key, params[key]));
fetch(Ip, {
  mode: 'no-cors' // 'cors' by default
})
.then(data=>{return data.json()})
.then(res=>{console.log(res);document.getElementById('trip').innerHTML = data})
.catch(error=>{console.log(error);})
distance_params = {query:'distance'};
Object.keys(distance_params).forEach(key => Ip.searchParams.append(key, params[key]));
fetch(Ip, {
  mode: 'no-cors' // 'cors' by default
})
.then(data=>{return data.json()})
.then(res=>{console.log(res);document.getElementById('distance').innerHTML = data})
.catch(error=>{console.log(error);})
duration_params = {query:'duration'};
Object.keys(duration_params).forEach(key => Ip.searchParams.append(key, params[key]));
fetch(Ip, {
  mode: 'no-cors' // 'cors' by default
})
.then(data=>{return data.json()})
.then(res=>{console.log(res);document.getElementById('duration').innerHTML = data})
.catch(error=>{console.log(error);})
calories_params = {query:'calories'};
Object.keys(calories_params).forEach(key => Ip.searchParams.append(key, params[key]));
fetch(Ip, {
  mode: 'no-cors' // 'cors' by default
})
.then(data=>{return data.json()})
.then(res=>{console.log(res);document.getElementById('calories').innerHTML = data})
.catch(error=>{console.log(error);})
