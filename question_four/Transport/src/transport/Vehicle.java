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
class Vehicle {
    
    String name;
    Engine engine;
    
    private StringBuilder vehicleBuilder;
    
    public Vehicle(String name, Engine engine){
        this.name = name;
        this.engine = engine;
    }

    void start_with_Key() {
        vehicleBuilder = new StringBuilder("starting - ")
                .append(this.name)
                .append(" ")
                .append(this.engine.type)
                .append(" Engine ")
                .append(this.engine.capacity)
                .append(" Ltrs");
                
        System.out.println(vehicleBuilder.toString());
    }
    
}
