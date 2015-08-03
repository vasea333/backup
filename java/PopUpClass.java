import javax.swing.*;
public class PopUpClass
{
public static void main(String[] args)
{
	display();
	String Name = fetchName();
	JOptionPane.showMessageDialog(null, "You name is" +Name);
}
static void display(){
	JOptionPane.showMessageDialog(null, "This program will take your name input and spit it blak out.", "About this Program",
			           JOptionPane.QUESTION_MESSAGE);
}
static String fetchName()

{
	String fetchedName = "";
	fetchedName = JOptionPane.showInputDialog("Please enter your name!", "Name enter");
	return fetchedName;
 }
}




