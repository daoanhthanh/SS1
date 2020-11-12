import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
public class iteration_ex{
    public static void main(String[] args) {
        List<String> car = new ArrayList<String>();
        car.add("Mecerdes Benz");
        car.add("Kia Morning");
        car.add("BMW Lighning");
        Iterator<String> in = car.iterator();
        while(in.hasNext()){
            System.out.println(in.next());
        }
    }
}