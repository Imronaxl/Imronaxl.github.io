import pokemons.*;
import ru.ifmo.se.pokemon.Battle;

public class Main {
    public static void main(String[] args) {
        Battle battle = new Battle();
        Drampa drampa = new Drampa("Чужой", 10);
        Slowpoke slowpoke = new Slowpoke("Чужой1", 9);
        Slowking slowking = new Slowking("Чужой2", 9);
        Deino deino = new Deino("Хищник", 10);
        Zweilous zweilous = new Zweilous("Хищник1", 9);
        Hydreigon hydreigon = new Hydreigon("Хищник2", 9);
       
        battle.addAlly(drampa);
        battle.addAlly(slowpoke);
        battle.addAlly(slowking);
        battle.addFoe(deino);        
        battle.addFoe(zweilous);
        battle.addFoe(hydreigon);

        battle.go();
    }
}