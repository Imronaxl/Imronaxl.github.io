// import ru.ifmo.se.pokemon.*;
package pokemons;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

import attacks.Bulldoze;
import attacks.FireBlast;
import attacks.DreamEater;
import attacks.NastyPlot;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Slowking extends Pokemon {
    public Slowking(String name, int level) {
        super(name, level);
        this.setType(Type.WATER, Type.PSYCHIC);
        this.setStats(95, 75, 80, 100, 110, 30);
        this.setMove(new Bulldoze(), new FireBlast(), new DreamEater(), new NastyPlot());
    }
}
