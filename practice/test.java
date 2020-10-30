import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class test {
	public static void initialize() {
        Character[] arr;
		List<Character> st = new ArrayList<Character>(Arrays.asList(arr));
		for( char c = 'a'; c<= 'z' ; c++) {
			st.add(c);
        }
        arr = st.toArray();
		List<Character> cha = new ArrayList<Character>();
		for(int i = 0; i < st.size(); i+=2) {
			cha.add(arr[i]);
		}
	}
}
