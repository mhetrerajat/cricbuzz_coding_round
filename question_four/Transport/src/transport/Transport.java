/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package transport;

/**
 *
 * @author rajatmhetre
 */
public class Transport {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        Vehicle v1, v2,v3;
          
        v1 = new Car ("Ferrari", new Dieselengine(5));
	v2 = new Car ("Audi", new Petrolengine(6));
	v3 = new Ship ("Titanic", new Dieselengine(8));

	v1.start_with_Key();
	v2.start_with_Key();
	v3.start_with_Key();
    }
    
}
