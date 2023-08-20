import { createGraphs } from './generateGraphs.js';

const leftDateButton = document.querySelector('.leftButton');
const rightDateButton = document.querySelector('.rightButton');
const graphDateText = document.querySelector('.dateText');

let graphDate = "2018";
graphDateText.textContent = graphDate;
createGraphs(graphDate);

function btnClicked(e) {
    // if left button is clicked
    if (e.target.classList.contains('leftButton')) {
        // if graphDate is 2018, do nothing
        if (graphDate == "2018") {
            return;
        }
        // else, decrease graphDate by 1
        else {
            graphDate--;
            graphDateText.textContent = graphDate;
            createGraphs(graphDate);
        }
    }

    // if right button is clicked
    if (e.target.classList.contains('rightButton')) {
        // if date is 2022, do nothing
        if (graphDate == "2022") {
            return;
        } 
        // else, increase graphDate by 1
        else {
            graphDate++;
            graphDateText.textContent = graphDate;
            createGraphs(graphDate);
        }
    }
}

// Get the current year
const currentYear = new Date().getFullYear();

// Update the currentYear element's content
document.getElementById('currentYear').textContent = currentYear;

leftDateButton.addEventListener('click', btnClicked);
rightDateButton.addEventListener('click', btnClicked);