// import ru.ifmo.se.pokemon.*;
package pokemons;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

import attacks.Bite;
import attacks.Swagger;
import attacks.Crunch;
import attacks.WaterFall;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Drampa extends Pokemon {
    public Drampa(String name, int level) {
        super(name, level);
        this.setType(Type.NORMAL, Type.DRAGON);
        this.setStats(75, 60, 85, 135, 91, 36);
        this.setMove(new Waterfall(), new Crunch(), new Swagger(), new Bite());
    }
}
