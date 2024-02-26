package com.nht.activitytrackerserver.model.sensor;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import lombok.Builder;
import lombok.Data;

import java.time.LocalDateTime;

@Data
@Builder
public class SensorDataDto {

    private Long id;

    @NotNull
    private Float lightDensity;

    @NotNull
    private Float waterLevel;

    @NotNull
    private Float temperature;

    @NotNull
    private Float humiditySoil;

    @NotNull
    private Float humidityWeather;

    private LocalDateTime createdDate;
}
