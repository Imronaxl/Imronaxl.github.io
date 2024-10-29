// import ru.ifmo.se.pokemon.*;
package pokemons;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

import attacks.Bulldoze;
import attacks.FireBlast;
import attacks.DreamEater;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Slowpoke extends Pokemon {
    public Slowpoke(String name, int level) {
        super(name, level);
        this.setType(Type.WATER, Type.PSYCHIC);
        this.setStats(90, 65, 65, 40, 40, 15);
        this.setMove(new Bulldoze(), new FireBlast(), new DreamEater());
    }
}
