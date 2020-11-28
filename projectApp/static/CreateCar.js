         $(document).ready(function (){


                    $("#car_form").on('submit',function (e) {

                        console.log("test")
                        //serialize form
                        var serForm = $(this).serialize();


                        $.ajax({
                            type: 'POST',
                            url: "http://127.0.0.1:5000//car/create",
                            data: serForm,
                            success:function(response){
                                //reset form
                                $("#car_form")[0].reset();
                                console.log(response)


                                alert("SUCCESS\nCar added with success.")
                                console.log("Car added")

                            },
                            error:function(response){

                                alert("ERROR\n Something wrong happened.")
                                console.log("Something wrong happened")
                                console.log(response)

                            }
                        })

                        e.preventDefault();

                    })


            });



