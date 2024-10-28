// import ru.ifmo.se.pokemon.*;
package pokemons;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

import attacks.ScaryFace;
import attacks.DarkPulse;
import attacks.DoubleHit;
import attacks.Crunch;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Hydreigon extends Pokemon {
    public Hydreigon(String name, int level) {
        super(name, level);
        this.setType(Type.DARK, Type.DRAGON);
        this.setStats(92, 105, 90, 125, 90, 98);
        this.setMove(new ScaryFace(), new DarkPulse(), new DoubleHit(), new Crunch());
    }
}
