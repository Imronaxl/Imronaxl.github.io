// import ru.ifmo.se.pokemon.*;
package pokemons;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

import attacks.ScaryFace;
import attacks.DarkPulse;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Deino extends Pokemon {
    public Deino(String name, int level) {
        super(name, level);
        this.setType(Type.DARK, Type.DRAGON);
        this.setStats(52, 65, 50, 45, 50, 38);
        this.setMove(new ScaryFace(), new DarkPulse());
    }
}
