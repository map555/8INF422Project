$(document).ready(function (){



                  //Get query result on submit
            $('#send_car_maker').on('click', function(e){


                e.preventDefault();
                var car_maker=document.getElementById("car_maker").value;

                $.ajax({
                        type: "GET",
                        url:"http://127.0.0.1:5000//ajax/get_cars_by_maker",
                        data: {car_maker:car_maker},
                        success:function(response){

                        var table = ""

                        console.log(response.car_info)

                        //change result title
                            var resultTitle=document.getElementById("ResultTitle")
                            resultTitle.innerText="Result for: "+car_maker

                        for (i = 0; i < response.car_info.length; i++){
                            car = response.car_info[i]
                            console.log(car)


                            table += `<tr>
                                <td id="makerResult">${car.maker}</td>
                                <td id="modelResult">${car.model}</td>
                                <td id="trimResult">${car.cartrim}</td>
                                <td id="colorResult">${car.carcolor}</td>
                                <td id="yearResult">${car.caryear}</td>
                                <td id="conditionResult">${car.condition}</td>
                                <td id="mileageResult">${car.mileage}</td>
                                <td id="weightResult">${car.carweight}</td>
                                <td id="priceResult">${car.price}</td>
                                </tr>`
                        }

                        $("#resulttable tbody").html(table)

                        },
                        error : function(response){
                            console.log("It's not working")
                            console.log(response)
                         }
            })
            })
        });


