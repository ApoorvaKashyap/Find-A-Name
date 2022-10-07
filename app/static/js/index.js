function avail(name, json, indeterminate=false) {
    if (json[name] === "1" && indeterminate === false) {
        document.getElementById("avail_"+name).innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="24" height="24" viewBox="0 0 226 226" style=" fill:#000000;"><g transform=""><g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><path d="M0,226v-226h226v226z" fill="none"></path><g fill="#1abc9c"><path d="M178.91667,28.25h-131.83333c-10.40542,0 -18.83333,8.42792 -18.83333,18.83333v131.83333c0,10.40542 8.42792,18.83333 18.83333,18.83333h131.83333c10.40542,0 18.83333,-8.42792 18.83333,-18.83333v-131.83333c0,-10.40542 -8.42792,-18.83333 -18.83333,-18.83333zM94.16667,163.98183l-44.32425,-44.32425l13.31517,-13.31517l31.00908,31.00908l68.67575,-68.67575l13.31517,13.31517z"></path></g><path d="" fill="none"></path><path d="" fill="none"></path></g></g></svg>';
    } else if(json[name] === "0" && indeterminate === false) {
        document.getElementById("avail_"+name).innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="24" height="24" viewBox="0 0 172 172" style=" fill:#000000;"><g transform="translate(0.516,0.516) scale(0.994,0.994)"><g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="none" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><g fill="#1abc9c" stroke="#cccccc" stroke-linejoin="round"><path d="M152.15385,46.30769v79.38462c0,14.54868 -11.91286,26.46154 -26.46154,26.46154h-79.38462c-14.54868,0 -26.46154,-11.91286 -26.46154,-26.46154v-79.38462c0,-14.54868 11.91286,-26.46154 26.46154,-26.46154h79.38462c14.54868,0 26.46154,11.91286 26.46154,26.46154zM95.25121,86l23.15385,-23.15385l-9.25121,-9.2512l-23.15385,23.15385l-23.15385,-23.15385l-9.2512,9.2512l23.15385,23.15385l-23.15385,23.15385l9.2512,9.25121l23.15385,-23.15385l23.15385,23.15385l9.25121,-9.25121z"></path></g><path d="M0,172v-172h172v172z" fill="none" stroke="none" stroke-linejoin="miter"></path><g fill="#1abc9c" stroke="none" stroke-linejoin="miter"><path d="M125.69231,19.84615h-79.38462c-14.54868,0 -26.46154,11.91286 -26.46154,26.46154v79.38462c0,14.54868 11.91286,26.46154 26.46154,26.46154h79.38462c14.54868,0 26.46154,-11.91286 26.46154,-26.46154v-79.38462c0,-14.54868 -11.91286,-26.46154 -26.46154,-26.46154zM118.40505,109.15385l-9.25121,9.25121l-23.15385,-23.15385l-23.15385,23.15385l-9.2512,-9.25121l23.15385,-23.15385l-23.15385,-23.15385l9.2512,-9.2512l23.15385,23.15385l23.15385,-23.15385l9.25121,9.2512l-23.15385,23.15385z"></path></g><path d="" fill="none" stroke="none" stroke-linejoin="miter"></path></g></g></svg>';
    } else {
        document.getElementById("avail_"+name).innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="24" height="24" viewBox="0 0 172 172" style=" fill:#000000;"><g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z" fill="none"></path><g id="original-icon" fill="#1abc9c"><path d="M136.16667,21.5h-100.33333c-7.91917,0 -14.33333,6.41417 -14.33333,14.33333v100.33333c0,7.91917 6.41417,14.33333 14.33333,14.33333h100.33333c7.91917,0 14.33333,-6.41417 14.33333,-14.33333v-100.33333c0,-7.91917 -6.41417,-14.33333 -14.33333,-14.33333zM114.66667,93.16667h-57.33333c-3.956,0 -7.16667,-3.21067 -7.16667,-7.16667v0c0,-3.956 3.21067,-7.16667 7.16667,-7.16667h57.33333c3.956,0 7.16667,3.21067 7.16667,7.16667v0c0,3.956 -3.21067,7.16667 -7.16667,7.16667z"></path></g></g></svg>';
    }
};

function loader(){
    document.getElementById("avail_pypi").innerHTML = '<span class="loading"></span>';
    document.getElementById("avail_npm").innerHTML = '<span class="loading"></span>';
    document.getElementById("avail_rubyGems").innerHTML = '<span class="loading"></span>';
    document.getElementById("avail_cpp").innerHTML = '<span class="loading"></span>';
    document.getElementById("avail_github").innerHTML = '<span class="loading"></span>';
    document.getElementById("avail_aur").innerHTML = '<span class="loading"></span>';
    document.getElementById("avail_debian").innerHTML = '<span class="loading"></span>';
    document.getElementById("avail_launchpad").innerHTML = '<span class="loading"></span>';
}


document.getElementById('submitName').addEventListener('click', function(){
    loader();
    let requests = new XMLHttpRequest();
    let array = ['github', 'pypi', 'npm', 'rubyGems', 'cpp', 'aur', 'debian', 'launchpad']
    project = document.getElementById('projectName').value;
    requests.open('GET', 'https://find-a-name.herokuapp.com/find-a-name/api/v1/all?name='+project);
    requests.onload = function() {
        data = JSON.parse(this.response)
        console.log(data)
        array.forEach(element => {
            avail(element, data)
        });
    };
    requests.send();
    setTimeout(() => {
        if (requests.statusText !== "OK") {
            alert("Operation Timed Out");
            array.forEach(element => {
                avail(element,'401',true)
            });
        }
    }, 50000);
});


document.getElementById('projectName').addEventListener('keydown', function(event) {
    if (event.key === "Enter") {
        event.preventDefault()
        loader();
        let requests = new XMLHttpRequest();
        let array = ['github', 'pypi', 'npm', 'rubyGems', 'cpp', 'aur', 'debian', 'launchpad'];
        project = document.getElementById('projectName').value;
        requests.open('GET', 'https://find-a-name.herokuapp.com/find-a-name/api/v1/all?name='+project);
        requests.onload = function() {
            data = JSON.parse(this.response)
            console.log(data)
            array.forEach(element => {
                avail(element, data)
            });
        };
        requests.send();
        setTimeout(() => {
            if (requests.statusText !== "OK") {
                alert("Operation Timed Out");
                array.forEach(element => {
                    avail(element,'401',true)
                });
            }
        }, 50000);
    }
});
