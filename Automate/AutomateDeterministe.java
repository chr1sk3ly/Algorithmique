import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Automate {

    private Set<Character> alphabet ;
    private Set<String> etats ;
    private String etatInitial ;
    private Set<String> etatsFinaux ;
    private Map<String,Map<Character, String>> transition ;

    @Override 
    public String toString() {
        String s = "" ;
        for (String etat : this.transition.keySet()) {
            Map<Character,String> trans = this.transition.get(etat) ;
            for (char alph : trans.keySet()){
                s+=etat + " -- " + alph + " -->" + trans.get(alph) + "\n"  ;
            }
        }
        
        return s ;
    }

    // Question 1 : Implementation d'un automate
    public Automate(Set<Character> alphabet, Set<String> etats, String etatInitial, Set<String>etatsFinaux, Map<String,Map<Character, String>> transition){
        this.alphabet = alphabet ;
        this.etats = etats ;
        this.etatInitial = etatInitial ;
        this.etatsFinaux = etatsFinaux ;
        this.transition = transition ;
    }

    // Question 2 : Méthode reconnait(mot)
    public boolean reconnait(String mot) {
        Character car ;
        Set<String> nouvellesEtats = new HashSet<>(), etatsCourants = new HashSet<>() ;
        etatsCourants.add(this.etatInitial) ;

        for (int i = 0; i < mot.length() ; i++) {
            car = mot.charAt(i) ;
            for (String etat : etatsCourants) {
                if(! this.transition.containsKey(etat)) continue ;
                Map<Character, String> res = this.transition.get(etat) ;
                if(res.containsKey(car)) nouvellesEtats.add(res.get(car)) ;
            }

            etatsCourants = nouvellesEtats ;
            nouvellesEtats = new HashSet<>() ;
        }

        for (String etat : etatsCourants) {
            if (this.etatsFinaux.contains(etat)) return true ;
        }

        return false ;
    }

    public static  void question3() {
        Set <Character> alphabet = new HashSet() ;
        Set <String> etats = new HashSet<>() ;
        Set <String> etatsFinaux = new HashSet<>() ;
        Map<String, Map<Character, String>> transition = new HashMap<>() ;
        Map<Character, String> t1 = new HashMap<>(),t2 = new HashMap<>(),t3 = new HashMap<>() ;

        t1.put('b', "2") ; 
        t2.put('a', "2") ; t2.put('b', "3") ; 
        t3.put('b',"3"); t3.put('c', "2");

        alphabet.add('a') ; alphabet.add('b') ; alphabet.add('c') ;

        etats.add("1") ; etats.add("2") ; etats.add("3") ;

        etatsFinaux.add("3") ;

        transition.put("1", t1) ; 
        transition.put("2", t2) ; transition.put("2", t2) ;
        transition.put("3",t3) ; transition.put("3",t3) ;

        Automate a = new Automate(alphabet, etats, "1", etatsFinaux, transition) ;

        System.out.println("bbb : "+a.reconnait("bbb")+ "\nbab : "+ a.reconnait("bab")+"\nbabcb : " + a.reconnait("babcb") + "\nbabbc : " + a.reconnait("babbc"));
    }

    public static void question4() {
        Map <Character, String> alphabetMap = new HashMap<>() ;

        alphabetMap.put('a', "a vu Pac-Man") ; alphabetMap.put('b', "a perdu Pac-Man") ;
        alphabetMap.put('c',"Pac-Man mange une super pac-gomme"); alphabetMap.put('d', "a Ã©tÃ© mangÃ© par Pac-Man") ;
        alphabetMap.put('e', "atteint la base"); alphabetMap.put('f', "Super pac-gomme expire") ;

        Set <Character> alphabet = new HashSet() ;
        Set <String> etats = new HashSet<>(Arrays.asList("Parcours le labrynthe", "Poursuit Pac-Man", "Fuit Pac-Man", "Retourne Ã  la base")) ;
        Set <String> etatsFinaux = new HashSet<>() ;
        Map<String, Map<Character, String>> transition = new HashMap<>() ;

        alphabet.add('a'); alphabet.add('b');alphabet.add('c');alphabet.add('d');alphabet.add('e');alphabet.add('f') ;

        Map<Character, String> t1 = new HashMap<>(),t2 = new HashMap<>(),t3 = new HashMap<>(), t4 = new HashMap<>() ;
        t1.put('a', "Poursuit Pac-Man") ; t1.put('c', "Fuit Pac-Man") ;
        t2.put('b', "Parcours le labrynthe") ; t2.put('c', "Fuit Pac-Man");
        t3.put('d', "Retourne Ã  la base") ; t3.put('f', "Parcours le labrynthe") ;
        t4.put('e', "Parcours le labrynthe") ;

        transition.put("Parcours le labrynthe", t1) ;
        transition.put("Poursuit Pac-Man", t2) ;
        transition.put("Fuit Pac-Man", t3) ;
        transition.put("Retourne Ã  la base", t4) ;

        Automate fantome = new Automate(alphabet, etats, "Parcours le labrynthe", etatsFinaux, transition) ;

       // System.out.println(fantome) ;

        print(fantome, alphabetMap) ;
    }

    public static void print(Automate automate, Map<Character, String> alphabetMap) {
        String s = "" ;
        for (String etat : automate.transition.keySet()) {
            Map<Character,String> trans = automate.transition.get(etat) ;
            
            for (char alph : trans.keySet()){
                String t = alphabetMap != null ? alphabetMap.get(alph) : String.valueOf(alph) ;
                s+=etat + " ---- " + t + " ----->" + trans.get(alph) + "\n"  ;
            }
        }
        System.out.println(s) ;
    }

}



public class AutomateDeterministe {
    public static void main(String args[]) {
        System.out.println("Hello World");
        Automate.question3() ;
        Automate.question4() ;
    }
}
