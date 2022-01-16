function myGame(userinput) {
    botinput =Math.floor(Math.random() * 3)+1;

    if(userinput==1){
        document.getElementById("userImage").src="{% static 'rock.PNG' %}";
    }
    if(userinput==2){
        document.getElementById("userImage").src="{% static 'Paper.PNG' %}";
    }
    if(userinput==3){
        document.getElementById("userImage").src="{% static 'Scissor.PNG' %}";
    }
    
    if(botinput==1){
        document.getElementById("botImage").src="{% static 'rock_bot.png' %}";
    }
    if(botinput==2){
        document.getElementById("botImage").src="{% static 'Paper_bot.png' %}";
    }
    if(botinput==3){
        document.getElementById("botImage").src="{% static 'Scissor_bot.png' %}";
    }
    
    if(userinput==1 & botinput==3 | userinput==2 & botinput==1| userinput==3 & botinput==2){
        document.getElementById("result").innerHTML='You Win';
    }
    if (botinput==1 & userinput==3 | botinput==2 & userinput==1| botinput==3 & userinput==2){
        document.getElementById("result").innerHTML='You Lost';
    }
    if(userinput==botinput){
        document.getElementById("result").innerHTML='Tie';
    }

}
