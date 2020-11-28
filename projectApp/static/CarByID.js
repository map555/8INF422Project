$(document).ready(function (){



                  //Get query result on submit
            $('#send_car_id').on('click', function(e){


                e.preventDefault();
                var car_id=document.getElementById("car_id").value;

                $.ajax({
                        type: "GET",
                        url:"http://127.0.0.1:5000//ajax/get_car_info_by_id",
                        data: {car_id:car_id},
                        success:function(response){
                            console.log("test")
                            console.log(response)
                            var car=response.car_info;
                            console.log(car)

                            console.log("It works")

                            $("#resulttable tbody").html(`<tr>
                                <td id="makerResult">${car.maker}</td>
                                <td id="modelResult">${car.model}</td>
                                <td id="trimResult">${car.cartrim}</td>
                                <td id="colorResult">${car.carcolor}</td>
                                <td id="yearResult">${car.caryear}</td>
                                <td id="conditionResult">${car.condition}</td>
                                <td id="mileageResult">${car.mileage}</td>
                                <td id="weightResult">${car.carweight}</td>
                                <td id="priceResult">${car.price}</td>
                                </tr>`)

                        },
                        error : function(response){
                            console.log("It's not working")
                            console.log(response)

                         }
            })
            })
        });



