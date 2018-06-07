let scheduler;
class DomObject{
    constructor($object){
        this.dom=$object;
    }
    changeCss(pack){
        this.dom.css(pack);
    }
    newChild($child,after=""){
        if(after==""){this.dom.append($child)}else{
        this.dom.children().eq(after).after($child);}
        return $child
    };
    removeChild(which){
        this.dom.children().eq(which).remove();
    }
}

class Scheduler extends DomObject{
    constructor($object){
        super($object)
        this.initialize()
    }
    initialize(){
        this.newChild($('<div id = "weekday-wrap" class = "mainwrap"></div>'))
        this.newChild($('<div id = "todo-wrap" class = "mainwrap"></div>'))
        this.newChild($('<div id = "schedule-wrap" class = "mainwrap"></div>'))
        for( let i = 0 ; i < 7 ; i++ ){
            this.dom.children(0).eq(0).append($('<div class = "weekday">'+'월화수목금토일'.slice(i,i+1)+'</div>'))
        }
        for( let i = 0 ; i < 5 ; i++ ){
            this.dom.children(0).eq(1).append($('<div class = "todoline"></div>'))
            for( let j = 0 ; j < 7 ; j++ ){
                this.dom.children(0).eq(1).children().eq(i).append($('<div class = "todo">&nbsp</div>'))
            }
        }
        for( let i = 0 ; i < 19 ; i++ ){
            this.dom.children(0).eq(2).append($('<div class = "timeline"></div>'))
            for( let j = 0 ; j < 7 ; j++ ){
                this.dom.children(0).eq(2).children().eq(i).append($('<div class = "dayline"></div>'))
                    this.dom.children(0).eq(2).children().eq(i).children().eq(j).append($('<div class = "minute">'+((i+7)%24).toString()+'</div>'))
                for( let  k = 1 ; k < 7 ; k ++ ){
                    this.dom.children(0).eq(2).children().eq(i).children().eq(j).append($('<div class = "minute">&nbsp</div>'))
                }
            }
        }

    }
}

$(document).ready(function(){
    scheduler = new Scheduler($('<div id = "scheduler"></div>'))
    $('#grid').append(scheduler.dom)

});
