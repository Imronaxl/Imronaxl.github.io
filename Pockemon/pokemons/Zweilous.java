// import ru.ifmo.se.pokemon.*;
package pokemons;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

import attacks.ScaryFace;
import attacks.DarkPulse;
import attacks.DoubleHit;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Zweilous extends Pokemon {
    public Zweilous(String name, int level) {
        super(name, level);
        this.setType(Type.DARK, Type.DRAGON);
        this.setStats(72, 85, 70, 65, 70, 58);
        this.setMove(new ScaryFace(), new DarkPulse(), new DoubleHit());
    }
}
